<Button label="Show" @click="showMessage" :disabled="visible" class="mb-4" />
<Message v-if="visible" severity="success" :life="3000">Auto Disappear Message</Message>