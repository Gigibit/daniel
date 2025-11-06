function openDialog(smsId, smsContent){
    document.querySelector('#sms-content').innerHTML = smsContent;
    const dialog = document.querySelector(`#dialog-1`);
    dialog.showModal();
    document.body.style.overflow = "hidden";
    document.documentElement.style.overflow = "hidden";
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



