<div class="flex-auto">
    <label for="ssn" class="font-bold block mb-2">SSN</label>
    <InputMask id="ssn" v-model="value1" mask="999-99-9999" placeholder="999-99-9999" fluid />
</div>

<div class="flex-auto">
    <label for="phone" class="font-bold block mb-2">Phone</label>
    <InputMask id="phone" v-model="value2" mask="(999) 999-9999" placeholder="(999) 999-9999" fluid />
</div>

<div class="flex-auto">
    <label for="serial" class="font-bold block mb-2">Serial</label>
    <InputMask id="serial" v-model="value3" mask="a*-999-a999" placeholder="a*-999-a999" fluid />
</div>