<template>
    <div>
        <ToggleSwitch v-model="checked1" />
        <ToggleSwitch v-model="checked2" :dt="amberSwitch" />
    </div>
</template>

<script setup>
import { ref } from 'vue';

const checked1 = ref(true);
const checked2 = ref(true);
const amberSwitch = ref({
    handle: {
        borderRadius: '4px'
    },
    colorScheme: {
        light: {
            root: {
                checkedBackground: '{amber.500}',
                checkedHoverBackground: '{amber.600}',
                borderRadius: '4px'
            },
            handle: {
                checkedBackground: '{amber.50}',
                checkedHoverBackground: '{amber.100}'
            }
        },
        dark: {
            root: {
                checkedBackground: '{amber.400}',
                checkedHoverBackground: '{amber.300}',
                borderRadius: '4px'
            },
            handle: {
                checkedBackground: '{amber.900}',
                checkedHoverBackground: '{amber.800}'
            }
        }
    }
});
</script>