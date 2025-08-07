<DatePicker v-model="buttondisplay" showIcon fluid :showOnFocus="false" />
<DatePicker v-model="icondisplay" showIcon fluid iconDisplay="input" />
<DatePicker v-model="templatedisplay" showIcon fluid iconDisplay="input" timeOnly>
    <template #inputicon="slotProps">
        <i class="pi pi-clock" @click="slotProps.clickCallback" />
    </template>
</DatePicker>