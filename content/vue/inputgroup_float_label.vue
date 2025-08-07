<InputGroup>
    <InputGroupAddon>
        <i class="pi pi-user"></i>
    </InputGroupAddon>
    <FloatLabel>
        <InputText id="over_label" v-model="value1" />
        <label for="over_label">Over Label</label>
    </FloatLabel>
</InputGroup>

<InputGroup>
    <InputGroupAddon>$</InputGroupAddon>
    <FloatLabel variant="in">
        <InputText id="in_label" v-model="value2" />
        <label for="in_label">In Label</label>
    </FloatLabel>
    <InputGroupAddon>.00</InputGroupAddon>
</InputGroup>

<InputGroup>
    <InputGroupAddon>www</InputGroupAddon>
    <FloatLabel variant="on">
        <InputText id="on_label" v-model="value3" />
        <label for="on_label">On Label</label>
    </FloatLabel>
</InputGroup>