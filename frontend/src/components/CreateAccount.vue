<template>
    <div>
        <label for="username">Username: </label>
        <input v-model="username" type="text" id="username">
        <br>
        <label for="password">Password: </label>
        <input v-model="password" type="password" id="password">
        <br>
        <button @click="createAccount">Create Account</button>
    </div>
</template>

<script>
import { createAccount } from '@/api';

export default {
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        async createAccount() {
            try {
                const userData = {'username': this.username, 'password': this.password};
                const response = await createAccount(userData);
                console.log(response.data);
            } catch (error) {
                console.log('Error creating account:', error);
            }
        },
    },
};
</script>