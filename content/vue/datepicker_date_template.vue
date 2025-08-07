<DatePicker v-model="date">
    <template #date="slotProps">
        <strong v-if="slotProps.date.day > 10 && slotProps.date.day < 15" style="text-decoration: line-through">{{ slotProps.date.day }}</strong>
        <template v-else>{{ slotProps.date.day }}</template>
    </template>
</DatePicker>