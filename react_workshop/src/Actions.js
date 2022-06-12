import React from 'react'
import C from './constants'
import {v4} from 'uuid'

export const addGroup = (_name, _genre, _short_description, _founding_date, _description) => ({
    type: C.ADDGROUP,
    id: v4(),
    name: _name,
    genre: _genre,
    short_description: _short_description,
    founding_date: _founding_date,
    description: _description 
})

export const addGenre = (_name, _short_description, _description) => ({
    type: C.ADDGENRE,
    id: v4(),
    name: _name,
    short_description: _short_description,
    description: _short_description
})

export const upgradeAccount = (_firstname, _mi, _lastname, _address1, _address2, _city, _state, _zip, _creditcard, _securitynumber, _expiration) => ({
    type: C.UPGRADEACCOUNT,
    id: v4(),
    firstname: _firstname,
    mi: _mi,
    lastname: _lastname,
    address1: _address1,
    address2: _address2,
    city: _city,
    state: _state,
    zip: _zip,
    creditcard: _creditcard,
    securitynumber: _securitynumber,
    expiration: _expiration
})