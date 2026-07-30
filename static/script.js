
// =======================
// РЕЙТИНГ
// =======================


const stars = document.querySelectorAll(".stars span");


if(stars.length > 0){


    stars.forEach(star => {


        // Наведение

        star.addEventListener("mouseover", function(){


            let value = this.dataset.value;


            stars.forEach(s => {


                if(s.dataset.value <= value){

                    s.classList.add("active");

                }
                else{

                    s.classList.remove("active");

                }


            });


        });





        // Нажатие


        star.addEventListener("click", function(){


            let value = this.dataset.value;



            fetch("/rate", {


                method:"POST",


                headers:{


                    "Content-Type":"application/json"


                },


                body:JSON.stringify({


                    score:value


                })


            })



            .then(response => response.json())


            .then(data => {


                if(data.status==="success"){


                    location.reload();


                }


                if(data.status==="already"){


                    alert("Вы уже оценили сайт!");

                }


            })



            .catch(error => {


                console.log(error);


            });



        });



    });





    // убрать подсветку

    document.querySelector(".stars").addEventListener("mouseleave",()=>{


        stars.forEach(star=>{


            star.classList.remove("active");


        });


    });


}








// =======================
// ПЛАВАЮЩИЕ КОНТАКТЫ
// =======================


const contacts = document.querySelector(".contacts");



if(contacts){


window.addEventListener("scroll",()=>{


    if(window.scrollY > 250){


        contacts.classList.add("fixed");


    }

    else{


        contacts.classList.remove("fixed");


    }


});


}
