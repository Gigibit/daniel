let closeDialog = () => {
    document.querySelector('#dialog-1').close();
    document.body.style.removeProperty("overflow");
    document.documentElement.style.removeProperty("overflow");
}

function openDialog(id, phonenumber, delivery_date, address, city){
    document.querySelector('#input-phonenumber').value = phonenumber;
    document.querySelector('#input-delivery_date').value = delivery_date;
    document.querySelector('#input-address').value = address;
    document.querySelector('#input-city').value = city;


    const dialog = document.querySelector(`#dialog-1`);
    dialog.showModal();
    document.body.style.overflow = "hidden";
    document.documentElement.style.overflow = "hidden";
    dialog.querySelector('#submit').onclick = async () =>{
        try{    
            let response = await fetch('order/update', {
                method : 'POST',
                headers : {
                    'Content-Type': 'application/json; charset=utf-8"'
                },
                body: JSON.stringify({
                    'id' : id,
                    'phonenumber' : document.querySelector('#input-phonenumber').value,
                    'delivery_date' : document.querySelector('#input-delivery_date').value,
                    'address' : document.querySelector('#input-address').value,
                    'city' : document.querySelector('#input-city').value
                })
            })
            alert('Modifica effettuata correttamente')
            location.reload()
            closeDialog()
        } catch (error) {
            console.error(error);
        }
    }
    document.querySelector(".closeDialog").addEventListener("click", () => {
        dialog.close();
        document.body.style.removeProperty("overflow");
        document.documentElement.style.removeProperty("overflow");
      })
}

window.addEventListener('load', ()=>{
    document.querySelectorAll("[data-dialog]").forEach(button => {
        button.addEventListener("click", ()=> {
   
          
          document.querySelector(".closeDialog").addEventListener("click", () => {
            dialog.close();
            document.body.style.removeProperty("overflow");
            document.documentElement.style.removeProperty("overflow");
          })
        })
    })
})
