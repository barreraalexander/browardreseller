var open_ann=false;var exp_btn=document.querySelector('#maxim_svg_ctnr');var exp_sect=document.querySelector('#index_section1')
var slider_ctnr=exp_sect.querySelector('#ann_slider_ctnr')
console.log(slider_ctnr);function modAnnouncements(){console.log('run');if(open_ann==false){exp_sect.style.height='15em';open_ann=true;}else if(open_ann==true){exp_sect.style.height='initial'
open_ann=false;}}
exp_btn.addEventListener('click',modAnnouncements);