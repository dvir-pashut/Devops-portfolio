db.createUser(
    {
        user  : "dvir",
        pwd   : " password",
        roles : [
            {
            role : "readwrite",
            db   : "dvirstore"
            }
        ]
    }
)