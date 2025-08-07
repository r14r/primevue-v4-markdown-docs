<InputGroup class="md:w-80">
    <InputGroupAddon>
        <i class="pi pi-shopping-cart"></i>
    </InputGroupAddon>
    <IftaLabel>
        <InputNumber v-model="value" inputId="price" mode="currency" currency="USD" locale="en-US" />
        <label for="price">Price</label>
    </IftaLabel>
</InputGroup>