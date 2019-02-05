/*global $,console*/
$(document).ready(function () {
    "use strict";
    $("html").niceScroll();
    
    $(".faOption").click(function () {
        $(".color-option").fadeToggle();
    }); 
    
    
    
    var colorLi = $(".option-box .color-option ul li");
    colorLi.eq(0).css("backgroundColor", "#da232e").end()
        .eq(1).css("backgronudColor", "green").end()
        .eq(2).css("backgronudColor", "yellow").end()
        .eq(3).css("backGronudColor", "blue");
    colorLi.click(function () {
        $("Link[href*='hcolor']").attr("href", $(this).attr("data-value"));
        /*console.log($(this).attr("data-value"));
        console.log($("Link[href*='hcolor']"));*/
    });
    
    
    
    $(".loading .spinner").fadeOut(2000,function(){
         $(this).parent().fadeOut(2000,function(){
             $("body").css("overflow","auto");
         });
    });
    
    
    
    var scrollUp = $("#scroll-top");
    $(window).scroll(function(){
        console.log($(this).scrollTop());
        
         if($(this).scrollTop() >= 700){
             scrollUp.show(1000);
         }
        else{
            scrollUp.hide();
        }
    });
    
    $("#scroll-top").click(function(){
            $("html, body").animate({scrollTop:0}, 600);
        });
    
    $(".price-table .r1").click(function () {
        $(".price-table .z1").show(500);
        
    });
    $(".price-table .r2").click(function () {
        $(".price-table .z2").show(500);
        
    });
    $(".price-table .r3").click(function () {
        $(".price-table .z3").show(500);
        
    });
    /*****************/
    $(".read-more-hover .fa").click(function () {
        $(".price-table .z1").hide(500);
        
    });
    $(".read-more-hover .fa").click(function () {
        $(".price-table .z2").hide(500);
        
    });
    $(".read-more-hover .fa").click(function () {
        $(".price-table .z3").hide(500);
        
    });
    
    
});