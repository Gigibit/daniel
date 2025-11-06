
let closeDialog = () => {
    document.querySelector('#dialog-1').close();
    document.body.style.removeProperty("overflow");
    document.documentElement.style.removeProperty("overflow");
  }

var currentTemplate = document.querySelector('#sms-template').value
document.querySelectorAll("[data-dialog]").forEach(button => {
    button.addEventListener("click", ()=> {
        const dialog = document.querySelector(`#${button.dataset.dialog}`);
        dialog.showModal();
      
      document.body.style.overflow = "hidden";
      document.documentElement.style.overflow = "hidden";
      
      document.querySelector(".closeDialog").addEventListener("click", closeDialog)
    })
})

document.querySelector('#submit').onclick = async (e)=>{
    e.preventDefault()
    let template = document.querySelector('#sms-template').value
    if (currentTemplate === template){
        closeDialog()
        return
    } 
    currentTemplate = template
    template = template.replaceAll(/%data|%cliente|%CLIENTE|%DATA|%Data|%Cliente/gi, '%s')
    try{    
        let response = await fetch('sms-template', {
            method : 'POST',
            headers : {
                'Content-Type': 'application/json; charset=utf-8"'
            },
            body: JSON.stringify({text:template})
        })
        closeDialog()
    } catch (error) {
        console.error(error);
    }
}