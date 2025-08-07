<PickList v-model="products" dataKey="id" breakpoint="1400px">
    <template #option="{ option  }">
        {{ option.name }}
    </template>
</PickList>