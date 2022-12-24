<template>
  <div
    class="flex w-full h-full flex-col justify-center items-center gap-12 text-6xl"
  >
    <div>Tag some enoji</div>
    <div
      class="flex flex-row gap-4 flex-wrap items-center justify-center w-10/12"
    >
      <span
        class="text-7xl px-4"
        :class="isSelected(emoji) ? 'bg-green-500' : ''"
        v-for="emoji in emoji"
        :key="emoji.name"
        @mouseover="mouseOver"
        @mousedown="mouseDown"
        :id="emoji"
        >{{ emoji }}</span
      >
    </div>
    <div class="text-lg">
      Select 1 or more emoji and type some tags below (comma seperated)
    </div>
    <div id="range_text" class="text-lg">
      {{
        HasSelection
          ? "Type some tags below (comma seperated)"
          : "Select 1 or more emoji"
      }}
    </div>
    <div class="text-xl flex flex-row gap-8">
      <label for="types">Show types:</label>
      <select name="types" id="types" @change="refreshEmoji">
        <option value="mixed">Mixed</option>
        <option value="tagged">Tagged</option>
        <option value="untagged">Untagged</option>
      </select>
    </div>
    <div>
      <textarea
        id="sequence_tags"
        class="border-solid border-2 border-black text-lg"
        v-if="HasSelection"
      ></textarea>
    </div>
    <div>
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white text-2xl font-bold py-2 px-4 rounded"
        id="submit"
        v-if="HasSelection"
        @click="submitTags"
      >
        Submit
      </button>
    </div>
    <div class="text-xl w-1/4 flex">
      <div class="w-2/3">number of emoji</div>
      <input
        type="number"
        :value="count"
        @change="refreshEmoji"
        class="border-solid border-2 border-black text-lg w-1/3"
      />
    </div>
    <div></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      emoji: [],
      selection: [],
      count: 3,
    };
  },
  mounted() {
    const types = document.getElementById("types");
    fetch(
      `http://localhost:8000/api/emoji/?count=${this.count}&types=${types.value}`
    )
      .then((response) => response.json())
      .then((data) => {
        this.emoji = data.map((emoji) => {
          return emoji.value;
        });
      });
  },
  methods: {
    refreshEmoji(event) {
      const types = document.getElementById("types");
      if (typeof event.target.value === Number) {
        this.count = event.target.value;
      }
      fetch(
        `http://localhost:8000/api/emoji/?count=${this.count}&types=${types.value}`
      )
        .then((response) => response.json())
        .then((data) => {
          this.emoji = data.map((emoji) => {
            return emoji.value;
          });
        });
      this.selection = [];
    },

    mouseOver(e) {
      if (e.buttons === 1) {
        console.log(e.target.id);
        if (!this.isSelected(e.target.id)) {
          this.selection.push(e.target.id);
        } else {
          this.selection = this.selection.filter(
            (emoji) => emoji !== e.target.id
          );
        }
      }
    },
    mouseDown(e) {
      if (!this.isSelected(e.target.id)) {
        this.selection.push(e.target.id);
      } else {
        this.selection = this.selection.filter(
          (emoji) => emoji !== e.target.id
        );
      }
    },
    isSelected(emoji) {
      return this.selection.includes(emoji);
    },
    submitTags() {
      let tags = document.getElementById("sequence_tags").value;
      tags = tags.split(",");
      tags = tags.map((tag) => {
        return { value: tag.trim() };
      });
      for (let i = 0; i < this.selection.length; i++) {
        this.selection[i] = this.selection[i].trim();
        let data = {
          value: this.selection[0],
          tags: tags,
        };

        fetch(`http://localhost:8000/api/emoji/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("Success:", data);
            document.getElementById("sequence_tags").value = "";
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      }
    },
  },
  computed: {
    HasSelection() {
      return this.selection.length > 0;
    },
    // CheckSequence() {
    //   let len = this.selection.length;
    //   if (len > 1) {
    //     let count = 0;
    //     for (let i = 0; i < this.emoji.length; i++) {
    //       if (this.selection.includes(this.emoji[i])) {
    //         count += 1;
    //         if (count === len) {
    //           return true;
    //         }
    //       } else if (count > 0) {
    //         return false;
    //       }
    //     }
    //   }
    //   return true;
    // },
  },
};
</script>
