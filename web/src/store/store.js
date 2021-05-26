import { writable } from "svelte/store";

const savedWritable = (key, initialValue) => {
  const variable = writable(initialValue);

  const saved = localStorage.getItem(key);
  if (saved) {
    variable.set(JSON.parse(saved));
  }

  variable.subscribe((val) => {
    localStorage.setItem(key, JSON.stringify(val));
  });

  return variable;
};

export const user = savedWritable("user", null);
