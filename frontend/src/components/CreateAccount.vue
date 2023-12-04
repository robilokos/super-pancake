<template>
    <div>
        <button @click="createAccount">Create Account</button>
    </div>
</template>

<script>
import { createAccount } from '@/api';

export default {
    methods: {
        async createAccount() {
            try {
                const userData = {'username': 'test', 'password': 'testpw'}
                const response = await createAccount(userData);
                console.log(response.data);
            } catch (error) {
                console.log('Error creating account:', error)
            }
        },
    },
};
</script>