<OrderList v-model="products" dataKey="id" breakpoint="575px" pt:pcListbox:root="w-full sm:w-56">
    <template #option="{ option }">
        {{ option.name }}
    </template>
</OrderList>