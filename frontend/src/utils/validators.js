function valid_email(value) {
    const validator = /[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+/
    return validator.test(value)
}


function valid_password(value) {
    const validator = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$/
    return validator.test(value)
}


function valid_username(value) {
    const validator = /^[a-z0-9_-]{3,15}$/
    return validator.test(value)
}


export {
    valid_email,
    valid_password,
    valid_username
}