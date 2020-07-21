let base_url = '/api/projects/';
let fetchData = {
    headers: {
          'Content-Type': 'application/json'
    },
    credentials: 'same-origin'
}

export async function fetchProject(slug) {
    // context is for sapper preloading pass undefined if not used.

    //Retrieves a specific project by slug
    // this is okay since it will always run on the same host
    let url = base_url;

    // If there is a size specified we want to search for it.
    if(slug !== undefined) {
        url += `?slug=${slug}`
    }

    // Fetching the projects
    const res = await fetch(url, fetchData);

    const projectList = await res.json();

    if (projectList.length === 0){
        return undefined;
    }
    return projectList[0];
}

export async function fetchProjects(projectSize=undefined) {
    //@param projectSize: Must be of type string and values can only be SMALL, MEDIUM, LARGE (see getSize)
    //@param slug: Slug gets a specific project and this wont return a list

    let url = base_url;
    // If there is a size specified we want to search for it.
    if(projectSize !== undefined && projectSize !== "ALL") {
        url += `?size=${projectSize}`
    }

    // Fetching the projects
    const res = await fetch(url, fetchData);
    return await res.json();
}

export function getSize() {
    return [
		{
			name: "Large",
			value: "LARGE"
		},
		{
			name: "Medium",
			value: "MEDIUM"
		},
		{
			name: "Small",
			value: "SMALL"
		},
        {
			name: "All",
			value: "ALL"
		}
	]
}