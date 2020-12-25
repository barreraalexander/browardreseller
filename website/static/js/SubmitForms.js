function submitRemove ( model_id ){
    let remove_input = document.querySelector('#removing_id')
    remove_input.setAttribute('value', model_id);
    
    let submit_btn = document.querySelector('#submit_remove');
    submit_btn.click();
}