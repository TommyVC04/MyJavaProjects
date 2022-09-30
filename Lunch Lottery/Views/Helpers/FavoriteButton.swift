//
//  FavoriteButton.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 9/7/22.
//

import SwiftUI

struct FavoriteButton: View {
    @State private var isSet = false

    var body: some View {
        Button (action: {isSet = true} ){
            Text("Confirm")
        }
        .padding()
        .foregroundColor(.white)
        .background(Color.blue)
        .clipShape(RoundedRectangle(cornerRadius: 5))
        .confirmationDialog("Are you sure?", isPresented: $isSet, titleVisibility: .visible) {
            Button("Yes", role: .destructive) {
                replaceAndConfirm()
            }
            Button("Cancel", role: .cancel) {}
        }
    }
}

func replaceAndConfirm() {
    //ENTER LOTTERY
}

struct FavoriteButton_Previews: PreviewProvider {
    static var previews: some View {
        FavoriteButton()
    }
}
