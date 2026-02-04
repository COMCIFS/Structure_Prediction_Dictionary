import uuid
import sys

def generate_data_block_id(prefix="_csp.data_block_id"):
    """
    Generates a unique identifier.
    """
    unique_id = uuid.uuid4()
    return f"{prefix} {unique_id}"

if __name__ == "__main__":
    user_prefix = sys.argv[1] if len(sys.argv) > 1 else "_csp.data_block_id"

    print(generate_data_block_id(user_prefix))
