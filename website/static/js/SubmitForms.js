function submitRemove ( model_id ){
    let remove_input = document.querySelector('#removing_id')
    remove_input.setAttribute('value', model_id);
    
    let submit_btn = document.querySelector('#submit_remove');
    submit_btn.click();
}

function submitAdd ( model_id ){
    let add_input = document.querySelector('#item_id')
    add_input.setAttribute('value', model_id);
    
    let submit_atc = document.querySelector('#submit_atc');
    submit_atc.click();
}



var atc_form = document.querySelector('#atc_form')
if (atc_form){
    atc_form.addEventListener('submit', async function(event){
        event.preventDefault()

        let model_id = atc_form.querySelector('#item_id').getAttribute('value')
        
        const res = await fetch
        (`/api/add_to_cart`, {
            method:'POST',
            body: JSON.stringify(model_id),
            headers: {"Content-type": "application/json; charset=UTF-8"}
        })
        
        .then(res => res.json)
        .then(json => console.log(json))
        .catch(err => console.log(err))

        // alert(model_id)
    })
    // alert('atc_form_here')

}