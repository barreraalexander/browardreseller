// var open_ann = false;
// var exp_sect = document.querySelector('#index_section1');
// var slider_ctnr = exp_sect.querySelector('#ann_slider_ctnr');
// var max_btn = exp_sect.querySelector('#maxim_svg_ctnr');
// var min_btn = exp_sect.querySelector('#minim_svg_ctnr');
// console.log(slider_ctnr);
 
// function modAnnouncements (){
//     // if (open_ann==false){
//     //     // exp_sect.style.height = '15em';
//     //     open_ann = true;
//     // } else if (open_ann==true){
//     //     // exp_sect.style.height = 'initial'
//     //     open_ann = false;
//     // }
//     slider_ctnr.classList.toggle('invisible');
//     max_btn.classList.toggle('invisible');
//     min_btn.classList.toggle('invisible');
// }

// try{
//     exp_sect.addEventListener('click', modAnnouncements);
// }
// catch{
//     console.log ('wrong page');
// }


var coupon_input = document.querySelector('#coupon_code')
function modCouponInput (){
    var http = new XMLHttpRequest();
    http.open("GET", '/api/get_coupons')
    http.send();
    let coupon_code_progress = document.querySelector('#coupon_code_progress')
    coupon_code_progress.classList.remove("invisible")
    http.onreadystatechange=(e)=>{
        let response_text = JSON.parse(http.responseText);
        for (let elem of response_text){
            if (this.value == elem.coupon_code){
                coupon_code_progress.classList.remove("coupon_code_progressing")
                coupon_code_progress.style.backgroundColor = "green"
                return
            } else {
                coupon_code_progress.classList.add("coupon_code_progressing")
            }
        }
    }
}
coupon_input.addEventListener('keyup', modCouponInput, false);
