<script>
import axios from 'axios'

export default {
    props: ['basket', 'deleteFromBasket'],
    data() {
        return {
            error: '',
            name: '',
            surname: '',
            email: '',
            phone: ''
        }
    },
    computed: {
        getSumma() {
            return this.basket.reduce((total, next) => total + parseFloat(next.price), 0)
        }
    },
    methods: {
        sendData() {
            if(this.name.length < 2)
                this.error = 'Им\'я не менше 2 символів'
            else if(this.surname.length < 2)
                this.error = 'Прізвище не менше 2 символів'
            else if(!this.email.includes('@') || !this.email.includes('.'))
                this.error = 'Email неправильного типу'
            else if(this.phone.length < 2)
                this.error = 'Телефон не менше 2 символів'
            else if(this.basket.length == 0 || this.getSumma == 0)
                this.error = 'Корзина порожня'
            else {
                this.error = ''

                const data = {
                    'name': this.name,
                    'surname': this.surname,
                    'email': this.email,
                    'phone': this.phone,
                    'summa': this.getSumma,
                    'basket': JSON.stringify(this.basket)
                }
                axios.post('http://127.0.0.1:8000/api/order-add/', data)
                    .then(res => {
                        this.error = res.data.result

                        setTimeout(() => {
                            location.href = res.data.url
                        }, 700)
                    })
            }
        }
    }
}
</script>

<template>
  <div>
    <h1>Оформлення замовлення</h1>
    <div class="data">
        <div class="basket" v-if="this.basket.length > 0">
            <div class="item" v-for="el in basket" :key="el.slug">
                <img :src="'/img/' + el.image" :alt="el.title">
                <h3>{{ el.title }}</h3>
                <span>{{ el.price }}$</span>
                <button @click="deleteFromBasket(el.slug)">Видалити</button>
            </div>
            <span>Всього: {{ getSumma }}$</span>
        </div>
        <div v-else>
            <h2>Товаров нет</h2>
        </div>
        <form>
            <p class="error">{{ error }}</p>
            <input type="text" v-model="name" placeholder="Ваше ім'я">
            <input type="text" v-model="surname" placeholder="Ваше прізвище">
            <input type="email" v-model="email" placeholder="Ваш email">
            <input type="phone" v-model="phone" placeholder="Телефон">
            <button type="button" @click="sendData()">Купити</button>
        </form>
    </div>
  </div>
</template>

<style scoped>
.data {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 50px 0;
}

.data > div {
    width: 40%;
}

h1 {
    margin-top: 150px;
    font-weight: 400;
    font-size: 90px;
    text-align: center;
}
.item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.item img {
    width: 60px;
}
.item h3 {
    color: #52585c;
    font-size: 15px;
    text-align: center;
}
.item span {
    font-weight: 600;
    color: #323232;
}

.item button, form button {
    border: 0;
    background: rgb(186, 43, 43);
    border-radius: 5px;
    padding: 7px 12px;
    cursor: pointer;
    color: #fff;
}

.item button:hover {
    background: rgb(133, 28, 28);
}

.items > span {
    font-weight: 600;
    color: #206E5B;
}

form input {
    width: 300px;
    padding: 10px 15px;
    border: 1.5px solid #575d61;
    border-radius: 2px;
    background: #81898e;
    margin-bottom: 20px;
    display: block;
    color: #fff;
    outline: none;
    font-size: 15px;
}

form input::placeholder {
    color: rgba(64, 64, 64, 0.531);
}

form input:focus {
    border-color: #242424;
}

form button {
    background: #206E5B;
}

form button:hover {
    background: #134438;
}

.error {
    margin-bottom: 10px;
    color: rgb(181, 46, 46);
}
</style>