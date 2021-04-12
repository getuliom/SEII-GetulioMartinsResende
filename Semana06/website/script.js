const api_url="https://blockchain.info/ticker"

async function getbrl(){
    const response= await fetch(api_url);
    const data=await response.json();
    const {BRL}=data;
    document.getElementById('value').textContent=BRL.last;
    document.getElementById('tobrl').textContent=parseFloat(1/BRL.last).toFixed(8);
    document.getElementById('sats').textContent=parseFloat((1/BRL.last)*100000000).toFixed(0);

}
getbrl();