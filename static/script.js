const stars = document.querySelectorAll(".stars span");


stars.forEach(star => {


    // подсветка звёзд
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



    // отправка оценки
    star.addEventListener("click", function(){


        let value = this.dataset.value;



        fetch("/rate", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },


            body: JSON.stringify({

                score: value

            })


        })


        .then(response => response.json())


        .then(data => {


            if(data.status === "success"){

                location.reload();

            }


            if(data.status === "already"){

                alert("Вы уже оценили сайт!");

            }


        })



        .catch(error => {

            console.log(error);

        });


    });


});



// убрать подсветку
document.querySelector(".stars").addEventListener("mouseout", function(){


    stars.forEach(star => {

        star.classList.remove("active");

    });


});