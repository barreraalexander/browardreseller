var open_ann = false;
var exp_sect = document.querySelector('#index_section1');
var slider_ctnr = exp_sect.querySelector('#ann_slider_ctnr');
var max_btn = exp_sect.querySelector('#maxim_svg_ctnr');
var min_btn = exp_sect.querySelector('#minim_svg_ctnr');
console.log(slider_ctnr);
 
function modAnnouncements (){
    // if (open_ann==false){
    //     // exp_sect.style.height = '15em';
    //     open_ann = true;
    // } else if (open_ann==true){
    //     // exp_sect.style.height = 'initial'
    //     open_ann = false;
    // }
    slider_ctnr.classList.toggle('invisible');
    max_btn.classList.toggle('invisible');
    min_btn.classList.toggle('invisible');
}

exp_sect.addEventListener('click', modAnnouncements);