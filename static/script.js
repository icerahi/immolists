const BASE_URL="http://127.0.0.1:8000/api/"
const CREATE_URL="http://127.0.0.1:8000/api/create/"

window.onload=function(){
	let tbody=document.querySelector('#tbody')
//get data from table and show table
	axios.get(BASE_URL)
	.then(res => {

		res.data.forEach(contact =>{
			createTDElement(contact,tbody)
		})
	})
	.catch()

// add event listener for new contact
	let save=document.querySelector('#save')
	save.addEventListener('click',function(){
		create()
	})
}

//create new contact function
function create(){
	
	let name=document.querySelector('#name')
	let phone=document.querySelector('#phone')
	let email=document.querySelector('#email')

	let contact={
		xsrfHeaderName: "X-CSRFToken",
		name:name.value,
		email:email.value,
		phone:phone.value
	}
	console.log(contact)

	 
		axios.post(CREATE_URL,contact)
		.then(res => {
			let tbody=document.querySelector('#tbody')
			createTDElement(res.data,tbody)

			name.value=''
			phone.value=''
			email.value=''

		})
		.catch(err => console.log(err))
	 
}



// create TR elements
function createTDElement(contact,parentElement){


	const TR=document.createElement('tr')

	const tdName= document.createElement('td')

	tdName.innerHTML=contact.name
	TR.appendChild(tdName)

	const tdPhone= document.createElement('td')
	tdPhone.innerHTML=contact.phone
	TR.appendChild(tdPhone)

		const tdEmail= document.createElement('td')
	tdEmail.innerHTML=contact.email
	TR.appendChild(tdEmail)

	const tdAction= document.createElement('td')


	const tdEditBtn=document.createElement('button')
	tdEditBtn.className='btn btn-warning'
	tdEditBtn.innerHTML='Edit'
	tdEditBtn.addEventListener('click',function(){
		console.log('I am edit button')
	})

	tdAction.appendChild(tdEditBtn)

	const tdDeleteBtn=document.createElement('button')
	tdDeleteBtn.className='btn btn-danger mx-1'
	tdDeleteBtn.innerHTML='Delete' 

	tdDeleteBtn.addEventListener('click',function(){

		console.log('I am delete button ')
	})

	tdAction.appendChild(tdDeleteBtn)

	TR.appendChild(tdAction)


	parentElement.appendChild(TR)
}
 
 

 