// Formset Javascript Implementation
const formset_table = document.getElementById('formset-table')
const addButton = document.getElementById('add-more')
addButton.addEventListener('click',add_new_form)
const totalForms = document.getElementById('id_form-TOTAL_FORMS')
// Adding the first non hidden form. 
add_new_form()

function countForms(){
    return formset_table.getElementsByClassName('product-form').length;
}

function remove_form(event){
    if (countForms() <= 1){
        return;
    }
    if (event.srcElement.tagName == "I" ){
        button = event.srcElement.parentNode;
    }
    else{
        button = event.srcElement;
    }
    button.parentNode.parentNode.remove();
    totalForms.setAttribute('value',countForms());
}


function add_new_form(event){
    if (event){
        event.preventDefault()
    }
    let number_of_forms = countForms()
    const new_form = document.getElementById('empty-form').cloneNode(true);
    new_form.hidden = false;
    elements = new_form.querySelectorAll('input,select,label,button')
    for (element of elements){
        attributes = element.attributes
        for (let i = 0; i<attributes.length; i++){
            element.setAttribute(attributes[i].name,attributes[i].value.replace('__prefix__',number_of_forms))
        }
    }
    for (input of new_form.querySelectorAll('input,select')){
        input.required = true
    }
    new_form.setAttribute('id','formset-'+number_of_forms)
    new_form.querySelector('#remove').addEventListener('click',remove_form)
    new_form.setAttribute('class','product-form')
    totalForms.setAttribute('value',number_of_forms+1) 
    formset_table.insertAdjacentElement('beforeend',new_form);
}

// Changing Client Name
let client = document.getElementById('id_client_name')
client.setAttribute('placeholder','Enter existing or new client name')

document.getElementById('id_place_name').labels.item(0).innerHTML = "Address:"