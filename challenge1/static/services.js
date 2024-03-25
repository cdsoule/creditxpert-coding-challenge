async function getColorSchemeById(id) {
    reponse = await fetch(`colors/${id}`)
    result = await reponse.json()

    return result
}

async function getShapeById(id) {
    reponse = await fetch(`shapes/${id}`)
    result = await reponse.json()

    return result
}