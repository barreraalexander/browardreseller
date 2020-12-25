//check if we're on inventory_item page
try{
    var submit_btn = document.querySelector('#submit_atc');
    submit_btn.addEventListener('click', addToCart)
} catch(err){
    console.log('not on item page')
}



function addToCart ( ) {
    let model_id = document.querySelector('#model_id').textContent;
    let item_key = getLatestIndex() + 1;

    localStorage.setItem(item_key, model_id);
    localStorage.setItem('latest', item_key);
    console.log(`set ${item_key}`);
}


function getLatestIndex ( ){
    latest_index = parseInt(localStorage.getItem('latest'));
    if (isNaN(latest_index)){
        return 0;
    } else {
        return latest_index;
    }
}


function getItem( index ){
    item = localStorage.getItem(index);
    return item;
}


function clearCart (){
    localStorage.clear();
}


function getCart ( ){
    highest_index = getLatestIndex();
    items = [];
    for (i = 0; i < highest_index; i++){
        item = getItem(i);
        items.push(item);
        alert (item);
    }
    return items;
}

//how it will work--