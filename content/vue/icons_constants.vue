<template>
    <div class="card flex justify-center">
        <Menu :model="items" />
    </div>
</template>

<script>
import { PrimeIcons } from '@primevue/core/api';

export default {
    data() {
        return {
            items: [
                {
                    label: 'File',
                    items: [
                        { label: 'New', icon: PrimeIcons.PLUS },
                        { label: 'Open', icon: PrimeIcons.DOWNLOAD }
                    ]
                }
            ]
        };
    }
};
</script>