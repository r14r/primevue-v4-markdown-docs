<PickList v-model="products" dataKey="id" breakpoint="1400px" scrollHeight="20rem">
    <template #option="{ option , selected }">
        <div class="flex flex-wrap p-1 items-center gap-4 w-full">
            <img class="w-12 shrink-0 rounded" :src="'https://primefaces.org/cdn/primevue/images/product/' + option.image" :alt="option.name" />
            <div class="flex-1 flex flex-col">
                <span class="font-medium text-sm">{{ option.name }}</span>
                <span :class="['text-sm', { 'text-surface-500 dark:text-surface-400': !selected, 'text-inherit': selected }]">{{ option.category }}</span>
            </div>
            <span class="font-bold">${{ option.price }}</span>
        </div>
    </template>
</PickList>