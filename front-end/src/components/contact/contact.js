function getContacts() {
    const imgFolder = "/contact"
    return [
        {
            name: "linkedin",
            img: `${imgFolder}/linkedin.svg`,
            link: "https://www.linkedin.com/in/lukas-van-den-berk-5b7681185/"
        },
        {
            name: "github",
            img: `${imgFolder}/github.svg`,
            link: "https://github.com/lukasvdberk"
        },
        {
            name: "mail",
            img: `${imgFolder}/mail.svg`,
            link: "mailto:lukasvdberk@gmail.com"
        },
    ]
}

export default getContacts