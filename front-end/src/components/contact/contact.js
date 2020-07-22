function getContacts() {
    const imgFolder = "/contact"
    return [
        {
            name: "Linkedin",
            img: `${imgFolder}/linkedin.svg`,
            link: "https://www.linkedin.com/in/lukas-van-den-berk-5b7681185/"
        },
        {
            name: "Github",
            img: `${imgFolder}/github.svg`,
            link: "https://github.com/lukasvdberk"
        },
        {
            name: "Email",
            img: `${imgFolder}/mail.svg`,
            link: "mailto:lukasvdberk@gmail.com"
        },
    ]
}

export default getContacts