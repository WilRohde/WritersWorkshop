export const group = (state = {}, action) => {
    switch (action.type) {
        case C.CREATE_GROUP:
        return {
            id: action.id,
            name: action.name,
            description: action.description,
            founding_date: action.founding_date,
            short_description: action.short_description,
            created_at: action.created_at,
            upated_at: action.updated_at,
            creator_id: action.creator_id,
            genre_id: action.genre_id,
            genre_name: action.genre_name
        }
    case C.UPDATE_GROUP:
    return {
        id: action.id,
        name: action.name,
        description: action.description,
        founding_date: action.founding_date,
        short_description: action.short_description,
        created_at: action.created_at,
        upated_at: action.updated_at,
        creator_id: action.creator_id,
        genre_id: action.genre_id,
        genre_name: action.genre_name
    }
    default:
        return state
    }
}
export const groups = (state = [], action) => {
    switch(action.type) {
        case C.GROUPS:
            return []
        default:
            return groups
    }
}
export const genres = (state = {}) => {
    switch(action.type) {
        case C.GENRES:
            return []
        default:
            return groups
    }
}