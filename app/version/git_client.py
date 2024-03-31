import subprocess
from app.version.git_data_model import GitData

class GitClient():
    def __init__(self):
        pass

    def get_git_info(self) -> GitData:
        """
        Get current Git commit hash and branch.

        Returns:
        tuple: A tuple containing the current commit hash and branch name.
            If an error occurs, returns (None, None).
        """
        try:
            # Get current commit hash
            commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
            
            # Get current branch name
            branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
            
            return GitData(commit=commit_hash, branch=branch)

        except subprocess.CalledProcessError:
            print("Error: Git command failed.")
