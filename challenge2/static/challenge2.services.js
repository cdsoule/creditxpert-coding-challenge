async function postMoves(k) {
    return await fetch('/challenge2/', {
        method: "POST",
        mode: "same-origin",
        headers: {
            "Content-Type": "application/JSON",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({"k": k})
    })
    .then((response) => {
        if (response.ok) {
            return response.json()
        } else if (response.status == 400) {
            return response.json()
                .then(errorData => {
                    throw new Error(errorData.message)
                })
        }
    })
    .then((data) => {
        return data
    })
    .catch(error => {
        alert(error)
    })
}