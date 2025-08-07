<InputGroup>
    <InputText placeholder="Price" />
    <InputGroupAddon>
        <RadioButton v-model="radioValue1" name="rb1" value="rb1" />
    </InputGroupAddon>
</InputGroup>

<InputGroup>
    <InputGroupAddon>
        <Checkbox v-model="checked1" :binary="true" />
    </InputGroupAddon>
    <InputText placeholder="Username" />
</InputGroup>

<InputGroup>
    <InputGroupAddon>
        <Checkbox v-model="checked2" :binary="true" />
    </InputGroupAddon>
    <InputText placeholder="Website" />
    <InputGroupAddon>
        <RadioButton v-model="radioValue2" name="rb2" value="rb2" />
    </InputGroupAddon>
</InputGroup>