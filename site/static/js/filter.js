    
if_filtered = false;
function CategoryFilter ( category ){
    let itemsCtnr = document.getElementById ("item-cards");
    let allcards = document.getElementsByClassName ("card");
    // let categoryCtnrs = itemsCtnr.getElementsByClassName (category);
    let opened = checkOpen ();

    
    if (if_filtered==false){
        let removed= {}
        var card;
        
        for (card in allcards){
            let curr_card = allcards[card]
            // alert (curr_card.classList)
            if (curr_card.classList.contains(category)){
            } else {
                // curr_card.classList.add ("invisible")
                removed.push(curr_card)
                curr_card.remove();
            }
        }
        if_filtered = true;
    
    } else if (if_filtered==true) {
        var elem = document.getElementById ("open_ctnr");
        let pressed_btn = document.getElementById (category)
        elem.classList.add ("invisible");
        homeCtnr.classList.remove ("invisible")
        pressed_btn.classList.remove ("pressed-btn")
        elem.id = category;
        is_open = false;
    }

function closeOpen (open){
    // loop through open, add invisible tag is not on there
}


function checkOpen (){
    var curr_open = document.getElementById ("open_ctnr");
    return curr_open
}

    // if ( query ) {
    //     homeCtnr.classList.add ("invisible");        
    //     recipeCtnr.classList.remove ("invisible");
    //     is_open = "true";
    //     alert (is_open)

    // } else if (is_open=="true") {
    //     alert ("both open")
    //     // homeCtnr.classList.remove ("invisible");
    //     // recipeCtnr.classList.add ("invisible")
    //     //pass
    // }
    //make container invisible or replace it with new recipe container
}

