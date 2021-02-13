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

