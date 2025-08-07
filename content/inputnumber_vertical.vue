<InputNumber v-model="value" showButtons buttonLayout="vertical" style="width: 3rem" :min="0" :max="99">
    <template #incrementbuttonicon>
        <span class="pi pi-plus" />
    </template>
    <template #decrementbuttonicon>
        <span class="pi pi-minus" />
    </template>
</InputNumber>