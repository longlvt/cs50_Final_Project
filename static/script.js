const name = document.getElementsByName("Username")
const password = document.getElementsByName("Password")
const form = document.getElementById("form")
const errorElement = document.getElementById("error")

form.addEventListener("submit", (event) => {
    let messages = []
    if (name.value === '' || name.value == null)
    {
        messaages.push('Name is required')
    }
    
    if (password.length <= 6)
    {
        messages.push('Password must be longer than 6 characters')
    }
    if (messages.length > 0)
    {
        event.preventDefault()
        errorElement.innerText = messages.join(', ')
    }
    

})