// Returns a list of strings of things about myself
async function getAboutMeTags() {

    const res = await fetch(
 '/api/about_tags/', {
            headers: {
              'Content-Type': 'application/json'
            },
            credentials: 'same-origin'
        }
    );

    const aboutMeTags = await res.json()
    return aboutMeTags.map(tag => tag["about_me"]);
    // return await res.json();
    // return [
    //     "Developer",
    //     "Front end dev",
    //     "Backend dev",
    //     "Linux enthousiast",
    //     "Home server owner",
    //     "Hard working guy",
    //     "Debian fan",
    //     "Docker lover",
    //     "Student",
    // ]
}

export default getAboutMeTags