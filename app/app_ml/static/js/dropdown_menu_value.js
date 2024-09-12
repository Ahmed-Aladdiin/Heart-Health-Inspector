age_dd = document.querySelector('#age')
chestPainType_dd = document.querySelector('#chestPainType')
restingECG_dd = document.querySelector('#restingECG')
st_slop_dd = document.querySelector('#st_slope')

ages = ``
for (let i = 1; i < 120; i++) {
  ages += `<option value="${i}">${i}</option>`
}
age_dd.innerHTML = ages

painType = ['NAP', 'ASY', 'TA', 'ATA']
painTypeHTML = ``

painType.forEach(i => {
  painTypeHTML += `<option value="${i}">${i}</option>`
});
chestPainType_dd.innerHTML = painTypeHTML

resting = ['Normal', 'LVH', 'ST']
restingHTML = ``

resting.forEach(i => {
  restingHTML += `<option value="${i}">${i}</option>`
});
restingECG_dd.innerHTML = restingHTML

slops = ['Down', 'Up', 'Flat']
slopsHTML = ``

slops.forEach(i => {
  slopsHTML += `<option value="${i}">${i}</option>`
});
st_slop_dd.innerHTML = slopsHTML