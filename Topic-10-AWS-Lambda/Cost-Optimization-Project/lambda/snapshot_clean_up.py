import boto3
from datetime import datetime, timezone


# Snapshots older than this number of days can be considered stale
RETENTION_DAYS = 30

# Safety switch
# True  = identify candidates but do not delete
# False = allow deletion of eligible snapshots
DRY_RUN = True

# Only snapshots with this tag are managed by this Lambda
MANAGED_BY_VALUE = "LambdaCostOptimization"


def lambda_handler(event, context):

    ec2 = boto3.client("ec2")

    response = ec2.describe_snapshots(
        OwnerIds=["self"]
    )

    snapshots = response["Snapshots"]

    print(f"Total snapshots found: {len(snapshots)}")
    print(f"Retention period: {RETENTION_DAYS} days")
    print(f"Dry-run mode: {DRY_RUN}")
    print(f"ManagedBy value: {MANAGED_BY_VALUE}")
    print("-" * 60)

    now = datetime.now(timezone.utc)

    managed_snapshots = 0
    protected_snapshots = 0
    retained_snapshots = 0
    deletion_candidates = 0
    deleted_snapshots = 0

    for snapshot in snapshots:

        snapshot_id = snapshot["SnapshotId"]
        volume_id = snapshot.get("VolumeId", "N/A")
        start_time = snapshot["StartTime"]

        # Convert tags into a dictionary
        tags = {
            tag["Key"]: tag["Value"]
            for tag in snapshot.get("Tags", [])
        }

        managed_by = tags.get("ManagedBy", "")
        retention_tag = tags.get("Retention", "")

        # Ignore snapshots not managed by this automation
        if managed_by != MANAGED_BY_VALUE:

            print(
                f"Snapshot {snapshot_id} ignored - "
                f"not managed by this Lambda."
            )

            continue

        managed_snapshots += 1

        # Calculate snapshot age
        age = now - start_time
        age_days = age.days

        # Protection rule
        if retention_tag.lower() == "keep":

            decision = "KEEP - PROTECTED"
            protected_snapshots += 1

        # Age rule
        elif age_days >= RETENTION_DAYS:

            decision = "DELETE CANDIDATE"
            deletion_candidates += 1

            # Actual deletion only happens when dry-run is disabled
            if not DRY_RUN:

                try:

                    ec2.delete_snapshot(
                        SnapshotId=snapshot_id
                    )

                    deleted_snapshots += 1

                    print(
                        f"DELETED: {snapshot_id}"
                    )

                except Exception as error:

                    print(
                        f"FAILED TO DELETE {snapshot_id}: {error}"
                    )

        else:

            decision = "KEEP"
            retained_snapshots += 1

        print(
            f"Snapshot ID: {snapshot_id}\n"
            f"Volume ID: {volume_id}\n"
            f"Age: {age_days} days\n"
            f"ManagedBy: {managed_by}\n"
            f"Retention: {retention_tag or 'None'}\n"
            f"Decision: {decision}\n"
        )

    print("-" * 60)
    print("CLEANUP SUMMARY")
    print(f"Snapshots examined: {len(snapshots)}")
    print(f"Managed snapshots: {managed_snapshots}")
    print(f"Protected snapshots: {protected_snapshots}")
    print(f"Retained snapshots: {retained_snapshots}")
    print(f"Deletion candidates: {deletion_candidates}")
    print(f"Deleted snapshots: {deleted_snapshots}")

    if DRY_RUN:

        print("DRY RUN ENABLED")
        print("No snapshots were deleted.")

    else:

        print("DELETE MODE ENABLED")

    return {
        "statusCode": 200,
        "body": (
            f"Analyzed {len(snapshots)} snapshots. "
            f"Deletion candidates: {deletion_candidates}. "
            f"Deleted: {deleted_snapshots}."
        )
    }