<Knob v-model="value" :size="150" readonly />
<div class="flex gap-2">
    <Button icon="pi pi-plus" @click="value++" :disabled="value >= 100" />
    <Button icon="pi pi-minus" @click="value--" :disabled="value <= 0" />
</div>