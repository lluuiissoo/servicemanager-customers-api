from fastapi import APIRouter
from app.version.semver import current_version
from app.version.version_service import get_git_data

router = APIRouter()

@router.get("", status_code=200)
async def version(ext: bool = False):

    result = {
        "version": current_version
    }

    if (ext):
        git_data = get_git_data()
        if (git_data):
            result["ext"] = {
                "commit": git_data.commit,
                "branch": git_data.branch
            }
        else:
            result["ext"] = {
                "commit": "",
                "branch": ""
            }
            
        # "version": current_version,
        # # "ext": {
        # #     "commit": git_data.commit,
        # #     "branch": git_data.branch
        # # }
            
    return result